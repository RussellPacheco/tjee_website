<template>
<div>
    <b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                View Messages
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
                    <template #cell(id)="data"><a v-b-modal.edit-modal>{{data.value}}</a></template>
                    <template #cell(created_by)="data"><a v-b-modal.edit-modal>{{data.value}}</a></template>
                    <template #cell(message)="data">{{data.value}}</template>
                    <template #cell(created_at)="data">{{data.value}}</template>
                    <template #cell(last_sent)="data">{{data.value}}</template>
                </b-table>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>                
    <b-modal ref="edit-modal" hide-header-close hide-footer no-close-on-backdrop title="Your Selected Message" size="lg">
        <b-container>
            <b-row>
                <b-col>
                    <b-row>
                        <b-col>
                            <b-row>
                                <b-table striped :items="[message]" :fields="modalFields"></b-table>
                            </b-row>
                        </b-col>
                    </b-row>
                    <b-row>
                        <b-col></b-col>
                        <b-col class="text-center mb-2 mt-3" id="modal-message">
                            <b>Message</b>
                        </b-col>
                        <b-col></b-col>
                    </b-row>
                    <b-row>
                        <b-col></b-col>
                        <b-col cols="10">{{message.message}}</b-col>
                        <b-col></b-col>
                    </b-row>
                </b-col>
            </b-row>
            <b-row class="mt-5">
                <b-col>
                    <b-button variant="success" @click="handleSend">Send Message</b-button>
                </b-col>
                <b-col class="d-flex justify-content-center">
                    <b-button variant="danger" @click="cancelModal">Cancel</b-button>
                </b-col>
                <b-col class="d-flex justify-content-end">
                    <b-button @click="handleEdit">Edit Message</b-button>
                </b-col>
            </b-row>
        </b-container>

    </b-modal>
</div>
  
</template>

<script>
export default {
    name: "ViewMessages",
    data() {
        return {
            message: {
                id: "",
                created_by: "",
                message: "",
                created_at: "",
                last_sent: ""
            },

            fields:[
                {key:"id", label:"ID"}, 
                {key: "created_by"}, 
                {key: "message", formatter: (value) => {return value.slice(0, 50).concat(" . . .")}}, 
                {key: "created_at"}, 
                {key: "last_sent"}
            ],

            items: this.$store.state.messages,

            modalFields: [
                {key:"id", label:"ID"}, 
                {key: "created_by"}, 
                {key: "created_at"}, 
                {key: "last_sent"}
            ],

        }
    },

    methods: {
        handleRowClick(item) {
            this.message = item
            this.$refs['edit-modal'].show()
        },

        handleSend() {
            this.$router.push({name: 'SendMessage'})

        },

        cancelModal() {
            this.$refs['edit-modal'].hide()
        },

        handleEdit() {
            this.$store.commit("setEditMessage", this.message)
            this.$router.push({name: 'EditMessage'})
        }

    }

}
</script>

<style>

#modal-message {
    border-bottom: 1px solid;
}

</style>