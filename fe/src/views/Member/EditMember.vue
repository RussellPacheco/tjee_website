<template>
<div>
<b-container class="mt-5">
    <b-row>
        <b-col></b-col>
        <b-col class="title text-center">
            Edit Member
        </b-col>
        <b-col></b-col>
    </b-row>
    <b-row class="mt-5">
        <b-col>
            <b-table striped :items="[this.$store.state.editMember]" :fields="modalFields"></b-table>
        </b-col>
    </b-row>
    <b-row>
        <b-col>
                <b-card bg-variant="light">
                    <b-form-group
                        label-cols-lg="3"
                        label="Please fill out all sections."
                        label-size="lg"
                        label-class="font-weight-bold pt-0"
                        class="mb-0"
                        >
                        <b-form-group                                
                            label-align="left"
                            label="First Name:"
                            label-for="firstname"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                            <b-form-input id="firstname" v-model="editMemberDetails.firstname.value"></b-form-input>
                        </b-form-group>
                        <b-form-group
                            label="Last Name:"
                            label-for="lastname"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                            <b-form-input id="lastname" v-model="editMemberDetails.lastname.value"></b-form-input>
                        </b-form-group>
                        <b-form-group
                            label="Gender:"
                            label-cols-sm="3"
                            label-align-sm="right"
                            class="mb-0"
                            v-slot="{ ariaDescribedby }"
                        >
                            <b-form-radio-group
                                id="gender-options"
                                class="pt-2"
                                :options="['Male', 'Female']"
                                :aria-describedby="ariaDescribedby"
                                v-model="editMemberDetails.gender.value"
                            ></b-form-radio-group>
                        </b-form-group>
                        <b-form-group
                            label="Country:"
                            label-for="country"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                            <b-form-input id="country" v-model="editMemberDetails.country.value"></b-form-input>
                        </b-form-group>
                        <b-form-group
                            label="Native Language:"
                            label-for="native-lang"
                            label-cols-sm="3"
                            label-align-sm="right"
                            v-slot="{ ariaLangList }"
                        >
                            <b-form-select
                                id="native-lang"
                                class="pt-2"
                                :options="langList"
                                :aria-describedby="ariaLangList"
                                v-model="editMemberDetails.nativeLang.value"
                            ></b-form-select>
                        </b-form-group>
                        <b-form-group
                            label="Learning Language:"
                            label-for="learning-lang"
                            label-cols-sm="3"
                            label-align-sm="right"
                            v-slot="{ ariaLearningLang }"
                        >
                            <b-form-select 
                                id="learning-lang" 
                                class="pt-2"
                                :options="['Japanese','English']"
                                :aria-describedby="ariaLearningLang"
                                v-model="editMemberDetails.learningLang.value">
                                </b-form-select>
                        </b-form-group>
                        <b-form-group
                            label="Line ID:"
                            label-for="line-id"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                            <b-form-input id="line-id" v-model="editMemberDetails.lineId.value"></b-form-input>
                        </b-form-group>
                        <b-form-group
                            label="Meetup Name:"
                            label-for="meetup-name"
                            label-cols-sm="3"
                            label-align-sm="right"
                        >
                            <b-form-input id="meetup-name" v-model="editMemberDetails.meetupName.value"></b-form-input>
                        </b-form-group>
                            <b-row class="mt-4">
                                <b-col class="d-flex justify-content-end">
                                </b-col>
                                <b-col class="d-flex justify-content-end">
                                    <b-button variant="danger" @click="handleClear">Clear</b-button>
                                    <b-button class="ml-3" variant="success" @click="handleConfirm">Confirm</b-button>
                                </b-col>
                            </b-row>
                    </b-form-group>
                </b-card>
        </b-col>
    </b-row>
    <b-modal hide-header-close no-close-on-backdrop @ok="handleSave" ref="save-modal" ok-title="Save" title="Save these details?">
        <b-row>
            <b-col>
                <div class="ml-5" v-for="(property, index) in editMemberDetails" :key="index">
                    {{property.name}}:
                </div>
            </b-col>
            <b-col>
                <div v-for="(property, index) in editMemberDetails" :key="index">
                    <b>{{ property.name == "ID" ? property.value.slice(0, 10) : property.value}}</b>
                </div>
            </b-col>
        </b-row>
    </b-modal>
</b-container>
</div>
</template>

<script>
import langList from "../../assets/data/lang.js"

export default {
    name: "EditMember",
    data() {
        return {
            langList: langList,
            editMemberDetails: {
                memberId: {name:"ID", value: this.$store.state.editMember.id},
                firstname: {name: "First Name", value: this.$store.state.editMember.firstname},
                lastname: {name: "Last Name", value: this.$store.state.editMember.lastname},
                gender: {name: "Gender", value: this.$store.state.editMember.gender},
                country:{name: "Country", value: this.$store.state.editMember.country},
                nativeLang: {name: "Native Language", value: this.$store.state.editMember.native_lang},
                learningLang: {name: "Learning Language", value: this.$store.state.editMember.lang_focus},
                lineId: {name: "Line ID", value: this.$store.state.editMember.line_id},
                meetupName: {name: "Meetup Name", value: this.$store.state.editMember.meetup_name},
                createdAt: {name: "Created At", value: this.$store.state.editMember.created_at}
            },
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
        handleOk(bvModalEvt) {
            bvModalEvt.preventDefault()
        },

        handleClear() {
            for (let item in this.editMemberDetails) {
                if (Object.prototype.hasOwnProperty.call(this.editMemberDetails, item)) {
                    this.editMemberDetails[`${item}`]["value"] = ""
                }
            }
        },

        handleConfirm() {
            if (this.formVerification()) {
                this.$refs['save-modal'].show()
            } else {
                this.$bvToast.toast('Please fill out all sections!', {
                    title: "Missing Details",
                    variant: "danger",
                    solid: true
                })
            }
        },

        handleSave() {
            const updateMember = {
                id: this.editMemberDetails.memberId.value,
                firstname: this.editMemberDetails.firstname.value,
                lastname: this.editMemberDetails.lastname.value,
                gender: this.editMemberDetails.gender.value,
                country: this.editMemberDetails.country.value,
                native_lang: this.editMemberDetails.nativeLang.value,
                lang_focus: this.editMemberDetails.learningLang.value,
                line_id: this.editMemberDetails.lineId.value,
                meetup_name: this.editMemberDetails.meetupName.value,
            }

            console.log(updateMember)

            this.$store.dispatch("updateMember", updateMember)

            this.$bvToast.toast("Member successfully updated!", {
                title: "Member Updated",
                variant: "success",
                solid: true
            })
        },

        formVerification() {
            let toggle = true
            for (let item in this.editMemberDetails) {
                if (this.editMemberDetails[item]["value"] == "") {
                    toggle = false
                }
            }
            if (!toggle) {
                return false
            } else {
                return true
            }
       }
    }

}
</script>

<style>

#edit-member-details {
    border: 1px solid;
    border-color: lightgray;
    border-radius: 3px;
}

#member-title {
    text-decoration: underline;
}


</style>