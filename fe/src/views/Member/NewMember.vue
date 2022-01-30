<template>
  <div id="new-member-container">
    <b-container  class="mt-5">
        <b-row class="mb-5">
            <b-col></b-col>
            <b-col cols="6" class="title text-center">
                Add New Member
            </b-col>
            <b-col></b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-row>
                    <b-col class="mb-4">
                        <b-card bg-variant="light">
                            <b-form-group
                                label="① Check"
                                label-size="lg"
                                label-class="font-weight-bold pt-0"
                                class="mb-0"
                            >
                                <b-form-group
                                    label="Is the new member in this list?"
                                    label-for="member-select"
                                    v-slot="{ memberSelect }"
                                >
                                    <b-form-select
                                        id="member-select"
                                        class=""
                                        :options="memberList"
                                        :aria-describedby="memberSelect"
                                        v-model="selectedMember"
                                        @change="updateForm"
                                    ></b-form-select>
                                </b-form-group>
                            </b-form-group>
                        </b-card>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="d-flex justify-content-center mb-4" id="imgBox">
                        <b-img rounded="circle" id="userImage" :src="selectedMember.photo.photo_link" />
                    </b-col>
                </b-row>                
            </b-col>
            <b-col>
                <b-card bg-variant="light">
                    <b-form-group
                        label-cols-lg="3"
                        label="➁ Fill out"
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
                                <b-form-input id="firstname" v-model="newMemberDetails.firstname.value"></b-form-input>
                            </b-form-group>

                            <b-form-group
                                label="Last Name:"
                                label-for="lastname"
                                label-cols-sm="3"
                                label-align-sm="right"
                            >
                                <b-form-input id="lastname" v-model="newMemberDetails.lastname.value"></b-form-input>
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
                                    v-model="newMemberDetails.gender.value"
                                ></b-form-radio-group>
                            </b-form-group>
                            <b-form-group
                                label="Country:"
                                label-for="country"
                                label-cols-sm="3"
                                label-align-sm="right"
                            >
                                <b-form-input id="country" v-model="newMemberDetails.country.value"></b-form-input>
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
                                    v-model="newMemberDetails.nativeLang.value"
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
                                    v-model="newMemberDetails.learningLang.value">
                                    </b-form-select>
                            </b-form-group>
                            <b-form-group
                                label="Line ID:"
                                label-for="line-id"
                                label-cols-sm="3"
                                label-align-sm="right"
                                v-b-popover.hover.top="'Must be unique'"
                            >
                                <b-form-input id="line-id" v-model="newMemberDetails.lineId.value"></b-form-input>
                            </b-form-group>
                            <b-form-group
                                label="Meetup Name:"
                                label-for="meetup-name"
                                label-cols-sm="3"
                                label-align-sm="right"
                                v-b-popover.hover.top="'Must be unique'"

                            >
                                <b-form-input id="meetup-name" v-model="newMemberDetails.meetupName.value"></b-form-input>
                            </b-form-group>
                                <b-row class="mt-4">
                                    <b-col class="d-flex justify-content-end">
                                    </b-col>
                                    <b-col class="d-flex justify-content-end">
                                        <b-button variant="danger" @click="handleClear">Clear</b-button>
                                        <b-button class="ml-3" variant="success" @click="handleSave">Submit</b-button>
                                    </b-col>
                                </b-row>
                    </b-form-group>
                </b-card>
            </b-col>
        </b-row>
        <b-modal hide-header-close no-close-on-backdrop @ok="handleConfirm" ref="confirm-modal" ok-title="Confirm" title="Please Confirm Details to Save">
            <b-row>
                <b-col>
                    <div class="ml-5" v-for="(property, index) in newMemberDetails" :key="index">
                        {{property.name}}:
                    </div>
                </b-col>
                <b-col>
                    <div v-for="(property, index) in newMemberDetails" :key="index">
                        <b>{{property.value}}</b>
                    </div>
                </b-col>
            </b-row>
        </b-modal>
    </b-container>
</div>
</template>

<script>
import langList from "../../assets/data/lang.js"
import { EventBus } from "../../utils"

export default {
    name: "NewMember",
    data() {
        return {
            status: 0,
            selectedMember: {photo: {photo_link: ""}},
            memberList: this.$store.state.unregisteredMembers.map(obj => { return {value: obj, text: obj.name} }),
            userImage: "https://secure.meetupstatic.com/photos/member/9/a/8/1/member_253599553.jpeg",
            newMemberDetails: {
                firstname: {name: "First Name", value: ""},
                lastname: {name: "Last Name", value: ""},
                gender: {name: "Gender", value: ""},
                country:{name: "Country", value: ""},
                nativeLang: {name: "Native Language", value: ""},
                learningLang: {name: "Learning Language", value: ""},
                lineId: {name: "Line ID", value: ""},
                meetupId: {name: "Meetup ID", value: ""},
                meetupName: {name: "Meetup Name", value: ""},
            },

            langList: langList
        }
    },
    methods: {
        handleClear() {
            for (let item in this.newMemberDetails) {
                if (Object.prototype.hasOwnProperty.call(this.newMemberDetails, item)) {
                    this.newMemberDetails[`${item}`]["value"] = ""
                }
            }
        },
        handleSave() {
            if (this.formVerification()) {
                this.$refs['confirm-modal'].show()
            } else {
                this.$bvToast.toast('Please fill out all sections!', {
                    title: "Missing Details",
                    variant: "danger",
                    solid: true
                })
            }
        },

        async handleConfirm() {
            const newMemberObj = {
                firstname: this.newMemberDetails.firstname.value,
                lastname: this.newMemberDetails.lastname.value,
                gender: this.newMemberDetails.gender.value,
                country: this.newMemberDetails.country.value,
                native_lang: this.newMemberDetails.nativeLang.value,
                lang_focus: this.newMemberDetails.learningLang.value,
                line_id: this.newMemberDetails.lineId.value,
                meetup_name: this.newMemberDetails.meetupName.value,
                meetup_id: this.newMemberDetails.meetupId.value
            }

            await this.$store.dispatch("saveNewMember", newMemberObj)

            if (this.status == 1) {
                this.$bvToast.toast('Member already exists', {
                    title: "Error!",
                    variant: "danger",
                    solid: true
                })
            } else if (this.status == -1) {
                this.$bvToast.toast('There was an error saving.', {
                    title: "Error!",
                    variant: "danger",
                    solid: true
                })
            } else {
                this.$bvToast.toast('Success!', {
                    title: "Member successfully created",
                    variant: "success",
                    solid: true
                })
                this.selectedMember = {photo: {photo_link: ""}},
                this.memberList = this.$store.state.unregisteredMembers.map(obj => { return {value: obj, text: obj.name} }),
                this.newMemberDetails = {
                    firstname: {name: "First Name", value: ""},
                    lastname: {name: "Last Name", value: ""},
                    gender: {name: "Gender", value: ""},
                    country:{name: "Country", value: ""},
                    nativeLang: {name: "Native Language", value: ""},
                    learningLang: {name: "Learning Language", value: ""},
                    lineId: {name: "Line ID", value: ""},
                    meetupId: {name: "Meetup ID", value: ""},
                    meetupName: {name: "Meetup Name", value: ""},
                }
            }
        },

        formVerification() {
            let toggle = true
            for (let item in this.newMemberDetails) {
                if (item != "meetupId") {
                    if (this.newMemberDetails[item]["value"] == "") {
                    toggle = false
                    }
                }
            }

            if (!toggle) {
                return false
            } else {
                return true
            }
        },
        updateForm() {
            if (this.selectedMember != "MEMBER DOESN'T EXIST") {
                for (let member of this.$store.state.unregisteredMembers) {
                    if (member["name"] == this.selectedMember["name"]) {
                        const fullname = member["name"].split(" ")
                        this.newMemberDetails = {
                            firstname: {name: "First name", value: fullname[0]},
                            lastname: {name: "Last name", value: fullname.length == 2 ? fullname[1] : ""},
                            gender: {name: "Gender", value: ""},
                            country:{name: "Country", value: member.country},
                            nativeLang: {name: "Native Language", value: ""},
                            learningLang: {name: "Learning Language", value: ""},
                            lineId: {name: "Line ID", value: ""},
                            meetupId: {name: "Meetup ID", value: member.id},
                            meetupName: {name: "Meetup Name", value: member.name},
                        }
                    }
                }                
            } else {
                this.newMemberDetails = {
                    firstname: {name: "First Name", value: ""},
                    lastname: {name: "Last Name", value: ""},
                    gender: {name: "Gender", value: ""},
                    country:{name: "Country", value: ""},
                    nativeLang: {name: "Native Language", value: ""},
                    learningLang: {name: "Learning Language", value: ""},
                    lineId: {name: "Line ID", value: ""},
                    meetupId: {name: "Meetup ID", value: ""},
                    meetupName: {name: "Meetup Name", value: ""},
                }
            }
        },        
    },

    mounted() {
        EventBus.$on('failedMemberCreation', (err) => {
            this.status = err
            this.$bvToast.toast("New member was not saved.", {
                title: "Error!",
                variant: "danger",
                solid: true
            })
        })
    },
    beforeDestroy () {
        EventBus.$off('failedMemberCreation')
  }
}
</script>

<style>

</style>