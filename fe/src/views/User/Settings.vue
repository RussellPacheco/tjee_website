<template>
<div>
<b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                Settings
            </b-col>
            <b-col></b-col>
        </b-row>
        <b-row>
            <b-col class="text-center">click on the selection to view more details</b-col>
        </b-row>
        <b-row class="mt-5">
            <b-col></b-col>
            <b-col sm="8" lg="8">
                <div class="accordion" role="tablist">
                    <b-card no-body class="mb-1">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-1 variant="dark">Change Password</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                                <b-form-group
                                    label="Current Password:"
                                    label-for="current-password"
                                    label-cols-sm="3"
                                    label-align-sm="right"
                                >
                                    <b-form-input type="password" id="current-password" v-model="password.currentPassword"></b-form-input>
                                </b-form-group>
                                <b-form-group
                                    label="New Password:"
                                    label-for="new-password"
                                    label-cols-sm="3"
                                    label-align-sm="right"
                                >
                                    <b-form-input type="password" id="new-password" v-model="password.newPassword"></b-form-input>
                                </b-form-group>
                                <b-form-group
                                    label="Retype New Password:"
                                    label-for="retype-password"
                                    label-cols-sm="3"
                                    label-align-sm="right"
                                >
                                    <b-form-input type="password" id="retype-password" v-model="password.retypePassword"></b-form-input>
                                </b-form-group>
                                <b-container>
                                    <b-row>
                                        <b-col></b-col>
                                        <b-col>
                                            <b-button @click="handleClear">Clear</b-button>
                                        </b-col>
                                        <b-col>
                                            <b-button @click="handleConfirm" variant="primary">Confirm</b-button>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card-body>
                        </b-collapse>
                    </b-card>
                    <b-card no-body class="mb-1">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-2 variant="dark">Add New Admin</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                            <b-card-body>
                                <b-form-group label="Choose Member:" label-for="new-admin" v-slot="{ariaMemberList}">
                                    <b-form-select id="new-admin" class="pt-2" :options="memberList" :aria-describedby="ariaMemberList" v-model="newAdmin"></b-form-select>
                                </b-form-group>
                                <b-container>
                                    <b-row>
                                        <b-col></b-col>
                                        <b-col></b-col>
                                        <b-col class="d-flex justify-content-end">
                                            <b-button @click="handleAdminConfirm" variant="danger">Confirm</b-button>
                                        </b-col>
                                    </b-row>
                                </b-container>
                            </b-card-body>
                        </b-collapse>
                    </b-card>
                </div>
            </b-col>
            <b-col></b-col>
        </b-row>
</b-container>
<b-modal hide-header-close no-close-on-backdrop @ok="handleSave" ref="save-modal" ok-variant="success" ok-title="Save" title="Are you sure you want to change your password?">
    <b-container>
        <b-row>
            <b-col class="d-flex justify-content-center">
                <img src="../../assets/img/idk.gif" />
            </b-col>
        </b-row>
    </b-container>
</b-modal>
<b-modal hide-header-close no-close-on-backdrop @ok="handleAdminSaveOk" id="new-admin-confirm-modal" ref="new-admin-confirm-modal" ok-variant="success" ok-title="Save" :title="'Please enter an admin username for '+ newAdminString +'.'">
    <b-container>
        <b-row>
            <b-col>
                <b-form ref="form" @submit.stop.prevent="handleAdminSave">
                    <b-form-group label="Username:" label-cols-lg="3" label-size="lg" label-class="pt-0" class="mb-0">
                        <b-form-input id="username" placeholder="Please enter a username..." v-model="adminUsername" :state="validation"></b-form-input>
                        <b-form-invalid-feedback>The username must be 5-12 characters long.</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label="Password:" label-cols-lg="3" label-size="lg" label-class="pt-0" class="mb-0">
                        <b-form-input id="password" placeholder="test123" disabled></b-form-input>
                    </b-form-group>
                </b-form>
            </b-col>
        </b-row>
    </b-container>
</b-modal>
<b-modal hide-header-close no-close-on-backdrop @ok="saveNewAdmin" ref="admin-save-modal" ok-variant="success" ok-title="Save" :title="'Are you sure you want to bestow Admin powers upon '+ newAdminString +'?'">
    <b-container>
        <b-row>
            <b-col class="d-flex justify-content-center">
                <img id="knight-img" src="../../assets/img/knight.gif" />
            </b-col>
        </b-row>
    </b-container>
</b-modal>
</div>  
</template>

<script>
import { EventBus } from "../../utils"

export default {
    name: "Setting",
    data() {
        return {
            status: 0,
            password: {
                currentPassword: "",
                newPassword: "",
                retypePassword: "",    
            }, 
            memberList: this.$store.state.members.map((member) => {
                const adminList = this.$store.state.admins.map(admin => admin.firstname)
                if(!adminList.includes(member.firstname)) {
                    return {
                        text: member.firstname + " " + member.lastname, 
                        value: member
                    }
                }
            }).filter(item => item != undefined),
            newAdmin: {},
            newAdminString: "",
            adminUsername: ""           
        }
    },
    computed: {
        validation() {
            if (this.adminUsername.length == 0) {
                return null
            } else if (this.adminUsername.length > 4 && this.adminUsername.length < 13) {
                return true
            } else {
                return false
            }
        },
    },
    methods: {
        handleClear() {
            for (let property in this.password) {
                this.password[property] = ""
            }

        },
        handleConfirm() {
            if (this.formVerification() && this.formVerification() != -1) {
                this.$refs['save-modal'].show()
            } else if (this.formVerification() == -1 ) {
                this.$bvToast.toast('Passwords don\'t match!', {
                    title: "New Password Inconsistency",
                    variant: "danger",
                    solid: true
                })
            } else {
                this.$bvToast.toast('Please fill out all sections!', {
                    title: "Missing Details",
                    variant: "danger",
                    solid: true
                })
            }
            

        },
        handleAdminConfirm() {
            if (this.newAdmin == "") {
                this.$bvToast.toast('No member selected!', {
                    title: "Please select a member.",
                    variant: "danger",
                    solid: true
                })
                
            } else {
                this.newAdminString = this.newAdmin.firstname.toString() + " " + this.newAdmin.lastname.toString()
                this.$refs['new-admin-confirm-modal'].show()
            }
        },
        handleAdminSaveOk(bvModalEvt) {
            bvModalEvt.preventDefault()
            this.handleAdminSave()
        },
        handleAdminSave() {
            if (this.adminUsername.length <= 4 || this.adminUsername.length > 12) {
                this.$bvToast.toast('Username length not sufficient!', {
                    title: "Please fix the username length.",
                    variant: "danger",
                    solid: true
                })
                return
            }
            this.$nextTick(() => {
                this.$bvModal.hide('new-admin-confirm-modal')
            })
            this.$refs['admin-save-modal'].show()
        },

        async handleSave() {
            const admin = {
                old_password: this.password.currentPassword,
                new_password: this.password.newPassword,
                username: this.$store.state.currentAdmin.username
            }
            await this.$store.dispatch("saveNewPassword", admin)
            if (this.status == 0) {
                this.password = {
                    currentPassword: "",
                    newPassword: "",
                    retypePassword: "",    
                }
                this.$bvToast.toast("Your password was changed.", {
                    title: "Success!",
                    variant: "success",
                    solid: true
                })
            }
        },

        async saveNewAdmin() {
            const newAdmin = {
                member_id: this.newAdmin.id,
                username: this.adminUsername,
                password: "test123"
            }
            await this.$store.dispatch("createNewAdmin", newAdmin)
            await this.$store.dispatch("getAdmins")

            this.memberList = this.$store.state.members.map((member) => {
                const adminList = this.$store.state.admins.map(admin => admin.firstname)
                if(!adminList.includes(member.firstname)) {
                    return {
                        text: member.firstname + " " + member.lastname, 
                        value: member
                    }
                }
            }).filter(item => item != undefined)
        },

        formVerification() {
            let toggle = true
            for (let property in this.password) {
                if (this.password[property] == "") {
                    toggle = false
                }
            }

            if (this.password.newPassword != this.password.retypePassword) {
                return -1
            }

            if (!toggle) {
                return false
            } else {
                return true
            }
       },

       toString(obj) {
           return obj.toString()

       }
    },

    mounted() {
        EventBus.$on('failedPassword', () => {
            this.status = 1
            this.$bvToast.toast("Error!", {
                title: "New password was not saved.",
                variant: "danger",
                solid: true
            })
        })
    },
    beforeDestroy () {
        EventBus.$off('failedPassword')
  }
}
</script>

<style>

</style>