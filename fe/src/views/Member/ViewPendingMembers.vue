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
            <b-col cols="16">
                <b-table striped hover :items="items" :fields="fields" @row-clicked="handleRowClick">
                    <template #cell(link)="data"><a :href="`${data.value}`">{{data.value}}</a></template>
                </b-table>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>                
    <b-modal ref="approvedeny-modal" hide-header-close no-close-on-backdrop hide-footer title="Would you like to approve or deny this" size="xl" ok-title="Get More Details" @ok="handleGetMoreDetails">
        <b-container>
            <b-row>
                <b-col>
                    <b-table striped :items="[pendingMember]" :fields="modalFields"></b-table>
                </b-col>
            </b-row>
            <b-row class="mt-5">
                <b-col>
                    <b-button variant="success" @click="handleApprove">Approve</b-button>
                </b-col>
                <b-col class="d-flex justify-content-center">
                    <b-button  @click="cancelModal">Cancel</b-button>
                </b-col>
                <b-col class="d-flex justify-content-end">
                    <b-button variant="danger" @click="handleDeny">Deny</b-button>
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
                meetup_name: "",
                app_date: "",
                link: ""
            },

            fields:[
                {key:"meetup_name", label: "Name"},
                {key:"app_date", label:"申請日"},
                {key:"answer_one", label:"Answer 1"},
                {key:"answer_two", label:"Answer 2"},
                {key:"answer_three", label:"Answer 3"},
                {key:"link", label:"Link"}
            ],

            items: this.$store.state.pendingMembers,

            modalFields: [
                {key:"meetup_name", label: "Name"},
                {key:"app_date", label:"申請日"},
                {key:"answer_one", label:"Answer 1"},
                {key:"answer_two", label:"Answer 2"},
                {key:"answer_three", label:"Answer 3"},
                {key:"link", label:"Link"}
            ],

        }
    },

    methods: {
        handleRowClick(item) {
            this.pendingMember = item
            this.$refs['approvedeny-modal'].show()
        },

        cancelModal() {
            this.$refs['approvedeny-modal'].hide()
        },

        handleGetMoreDetails() {
            this.$store.commit("setPendingMember", this.pendingMember)
            this.$router.push({name: 'PendingMemberDetails'})
        },

        handleApprove() {
            this.$store.dispatch("approvePendingMember", this.pendingMember)
            this.$refs['approvedeny-modal'].hide()
        },
        handleDeny() {
            this.$store.dispatch("denyPendingMember", this.pendingMember)
            this.$refs['approvedeny-modal'].hide()
        }


    }

}
</script>

<style>

#modal-message {
    border-bottom: 1px solid;
}

</style>