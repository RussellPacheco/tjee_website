<template>
<div>
    <b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                View Permissions
            </b-col>
            <b-col></b-col>
        </b-row>
        <b-row>
            <b-col class="text-center">click on the row to view more details</b-col>
        </b-row>
    </b-container>
    <b-container>
        <b-row class="mt-5">
            <b-col></b-col>
            <b-col cols="10">
                <b-table striped hover :items="items" :fields="fields" @row-clicked="handleRowClick">
                </b-table>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>                
    <b-modal ref="edit-modal" hide-header-close ok-title="Save" @ok="handleOk" no-close-on-backdrop title="Your Selected Permission" size="lg">
        <b-container>
            <b-row>
                <b-col>
                    <b-row>
                        <b-col>
                            <b-row>
                                <b-table striped :items="[botPermissions]" :fields="modalFields"></b-table>
                            </b-row>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col></b-col>
                        <b-col class="text-center mb-2 mt-3" id="modal-permission">
                            <b>New Permission Value</b>
                        </b-col>
                        <b-col></b-col>
                    </b-row>
                    <b-row>
                        <b-col></b-col>
                        <b-col class="d-flex justify-content-center"><b-form-select v-model="selected" :options="options"></b-form-select></b-col>
                        <b-col></b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-container>

    </b-modal>
</div>
  
</template>

<script>
export default {
    name: "Permissions",
    data() {
        return {
            botPermissions: {
                permission_name: "",
                permission_value: "",
                last_modified: ""
            },

            fields:[
                {key: "permission_name"}, 
                {key: "permission_value", formatter: value => {return value.toString().toUpperCase()}, class: 'text-center'}, 
                {key: "last_modified"}
            ],

            items: this.$store.state.botPermissions,

            modalFields: [
                {key: "permission_name"}, 
                {key: "permission_value", formatter: value => {return value.toString().toUpperCase()}, class: 'text-center'}, 
                {key: "last_modified"}
            ],

            selected: null,
            options: [
                {value: true, text: "TRUE"},
                {value: false, text: "FALSE"}
            ]

        }
    },

    methods: {
        handleRowClick(item) {
            this.botPermissions = item
            this.$refs['edit-modal'].show()
        },

        handleOk() {
            this.selected
        },

    }

}
</script>

<style>

#modal-permission {
    border-bottom: 1px solid;
}

</style>