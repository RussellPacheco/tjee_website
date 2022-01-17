<template>
<div class="login-container">
    <b-container>
        <b-row>
            <b-col></b-col>
            <b-col class="login p-5" cols="4">
                <b-form  @submit.stop.prevent>
                    <label for="feedback-user">User ID</label>
                    <b-form-input v-model="user.username" :state="validation" id="feedback-user"></b-form-input>
                    <b-form-invalid-feedback :state="validation">
                        Your user ID must be 5-12 characters long.
                    </b-form-invalid-feedback>
                    <label for="text-password">Password</label>
                    <b-form-input v-model="user.password" type="password" id="text-password" aria-describedby="password-help-block"></b-form-input>
                    <b-form-text id="password-help-block">
                        Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
                    </b-form-text>
                </b-form>
                <b-row>
                    <b-col></b-col>
                    <b-col></b-col>
                    <b-col class="mt-3"><b-button @click="login">Submit</b-button></b-col>
                </b-row>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>
</div>
</template>

<script>
import { EventBus } from "../../utils"

export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
            },

            errorMsg: ""

        }   
    },
    computed: {
        validation() {
            if (this.user.username.length == 0) {
                return null
            } else if (this.user.username.length > 4 && this.user.username.length < 13) {
                return true
            } else {
                return false
            }
        }
    },
    methods: {
        login: async function() {
            
            if (!this.inputCheck()) {
                this.$bvToast.toast("Please fill in all fields", {
                    title: "Error!",
                    variant: "danger",
                    solid: true
                })

                return 

            }
            
            await this.$store.dispatch('login', this.user)
            
            if (this.$store.state.adminLogin == true) {
                this.$router.push({name: "Admin"})
            } else {
                this.$bvToast.toast("Could not log in!", {
                    title: "Error!",
                    variant: "danger",
                    solid: true
                })
            }
        },

        inputCheck() {
            if (this.user.username == "" || this.user.password == "") {
                return false
            }

            return true
        }
        
    },
    mounted() {
        EventBus.$on('failedAuthentication', (msg) => {
            this.errorMsg = msg
        })
    },
    beforeDestroy () {
        EventBus.$off('failedAuthentication')
  }

}
</script>

<style>

.login {
    border-style: solid;
    border-radius: 8px;
    border-color: dimgray;

}

.login-container {
    margin-top: 12%;
}

</style>