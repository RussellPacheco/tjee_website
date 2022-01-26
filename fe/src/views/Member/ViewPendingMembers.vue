<template>
<div>
    <b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center" cols="8">
                View Pending Applications
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
            <b-col cols="12">
                <b-table striped hover :items="items" :fields="fields" @row-clicked="handleRowClick">
                    <template #cell(name)="data"><a v-b-modal.edit-modal>{{data.value}}</a></template>
                    <template #cell(app_date)="data">{{data.value}}</template>
                </b-table>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>                
    <b-modal ref="edit-modal" hide-header-close no-close-on-backdrop title="Your Selected Pending Member" size="lg" ok-title="Get More Details" @ok="handleGetMoreDetails">
        <b-container>
            <b-row>
                <b-col>
                    <b-table striped :items="[pendingMember]" :fields="modalFields"></b-table>
                </b-col>
            </b-row>
        </b-container>
    </b-modal>
</div>
  
</template>

<script>
export default {
    name: "ViewPendingMembers",
    data() {
        return {
            pendingMember: {
                id: "",
                name: "",
                app_date: "",
                link: ""
            },

            fields:[
                {key:"name", label: "Name"},
                {key:"app_date", label:"申請日"},
            ],

            items: this.$store.state.pendingMembers,

            modalFields: [
                {key:"name", label: "Name"},
                {key:"app_date", label:"申請日"},
            ],

        }
    },

    methods: {
        handleRowClick(item) {
            this.pendingMember = item
            this.$refs['edit-modal'].show()
        },

        cancelModal() {
            this.$refs['edit-modal'].hide()
        },

        handleGetMoreDetails() {46
            this.$store.commit("setPendingMember", this.pendingMember)
            this.$router.push({name: 'PendingMemberDetails'})
        }

    }

}
</script>

<style>

#modal-message {
    border-bottom: 1px solid;
}

</style>