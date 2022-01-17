<template>
<div>
    <b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                View Members
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
                    <template #cell(firstname)="data"><a v-b-modal.edit-modal>{{data.value}}</a></template>
                    <template #cell(lastname)="data">{{data.value}}</template>
                    <template #cell(gender)="data">{{data.value}}</template>
                    <template #cell(country)="data">{{data.value}}</template>
                    <template #cell(native_lang)="data">{{data.value}}</template>
                    <template #cell(lang_focus)="data">{{data.value}}</template>
                    <template #cell(line_id)="data">{{data.value}}</template>
                    <template #cell(meetup_name)="data">{{data.value}}</template>
                    <template #cell(created_at)="data">{{data.value}}</template>
                </b-table>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>                
    <b-modal ref="edit-modal" hide-header-close no-close-on-backdrop title="Your Selected Member" size="lg" ok-title="Edit Member" @ok="handleEdit">
        <b-container>
            <b-row>
                <b-col>
                    <b-table striped :items="[member]" :fields="modalFields"></b-table>
                </b-col>
            </b-row>
        </b-container>
    </b-modal>
</div>
  
</template>

<script>
export default {
    name: "ViewMembers",
    data() {
        return {
            member: {
                id: "",
                firstname: "",
                lastname: "",
                gender: "",
                country:"",
                native_lang:"",
                lang_focus:"",
                line_id: "",
                meetup_name: "",
                created_at: ""
            },

            fields:[
                {key:"firstname", label: "First Name"},
                {key:"lastname", label: "Last Name"},
                {key:"gender"},
                {key:"country"},
                {key:"native_lang", label:"Native Lang."},
                {key:"lang_focus", label:"Learning Lang."},
                {key:"meetup_name"},
                {key: "created_at"}, 
            ],

            items: this.$store.state.members,

            modalFields: [
                {key:"firstname", label: "First Name"},
                {key:"lastname", label: "Last Name"},
                {key:"gender"},
                {key:"country"},
                {key:"native_lang", label:"Native Lang."},
                {key:"lang_focus", label:"Learning Lang."},
                {key:"meetup_name"},
                {key: "created_at"}, 
            ],

        }
    },

    methods: {
        handleRowClick(item) {
            this.member = item
            this.$refs['edit-modal'].show()
        },

        cancelModal() {
            this.$refs['edit-modal'].hide()
        },

        handleEdit() {
            this.$store.commit("setEditMember", this.member)
            this.$router.push({name: 'EditMember'})
        }

    }

}
</script>

<style>

#modal-message {
    border-bottom: 1px solid;
}

</style>