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
            <b-col></b-col>
            <b-col cols="10">
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
                            >
                                <b-form-input id="learning-lang" v-model="newMemberDetails.learningLang.value"></b-form-input>
                            </b-form-group>
                            <b-form-group
                                label="Line ID:"
                                label-for="line-id"
                                label-cols-sm="3"
                                label-align-sm="right"
                            >
                                <b-form-input id="line-id" v-model="newMemberDetails.lineId.value"></b-form-input>
                            </b-form-group>
                            <b-form-group
                                label="Meetup Name:"
                                label-for="meetup-name"
                                label-cols-sm="3"
                                label-align-sm="right"
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
            <b-col></b-col>
        </b-row>
        <b-modal hide-header-close no-close-on-backdrop @ok="handleConfirm" ref="confirm-modal" ok-title="Confirm" title="Please Confirm Details to Save">
            <b-row>
                <b-col>
                    <div class="ml-5" v-for="property in newMemberDetails" :key="property">
                        {{property.name}}:
                    </div>
                </b-col>
                <b-col>
                    <div v-for="property in newMemberDetails" :key="property">
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

export default {
    name: "NewMember",
    data() {
        return {
            newMemberDetails: {
                firstname: {name: "First Name", value: ""},
                lastname: {name: "Last Name", value: ""},
                gender: {name: "Gender", value: ""},
                country:{name: "Country", value: ""},
                nativeLang: {name: "Native Language", value: ""},
                learningLang: {name: "Learning Language", value: ""},
                lineId: {name: "Line ID", value: ""},
                meetupName: {name: "Meetup Name", value: ""},
            },

            langList: langList
        }
    },
    methods: {
        handleClear() {
            this.firstname = ""
            this.lastname = ""
            this.gender = ""
            this.country = ""
            this.nativeLang = ""
            this.learningLang = ""
            this.lineId = ""
            this.meetupName = ""
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

        formVerification() {
            if (this.firstname == "" || this.lastname == "" || this.gender == "" || 
            this.country == "" || this.nativeLang == "" || this.learningLang == "" ||
            this.lineId == "" || this.meetupName == "") {
                return false
            } else {
                return true
            }
        }
    }
}
</script>

<style>

</style>