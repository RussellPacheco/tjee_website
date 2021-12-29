<template>
<div>
    <b-container class="mt-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                Send Message
            </b-col>
            <b-col></b-col>
        </b-row>
        <b-row class="mt-5">
            <b-col class="text-center">Would you like to</b-col>
        </b-row>
        <b-row>
            <b-col class="d-flex justify-content-center mt-5"><b-button variant="success">Send the message immediately</b-button></b-col>
        </b-row>
        <b-row class="text-center">
            <b-col id="or" class="mt-5">Or</b-col>
        </b-row>
        <b-row>
            <b-col class="d-flex justify-content-center mt-5">
                <b-button variant="warning" @click="handleSchedule">Schedule the message date and time</b-button>
            </b-col>
        </b-row>
        <b-row id="schedule" v-if="showSchedule">
            <b-col class="d-flex justify-content-end mt-5">
                <b-calendar v-model="date" @context="onDateContext" locale="en-US"></b-calendar>
            </b-col>
            <b-col >
                <b-row>
                    <b-col class="d-flex justify-content-start mt-5">
                        <b-time v-model="time" locale="en" @context="onTimeContext"></b-time>
                    </b-col>
                </b-row>
                <b-row class="mt-3">
                    <b-col>
                        <b-button id="left-button" variant="danger" @click="handleReset">Reset</b-button>
                        <b-button variant="success" @click="handleSave">Save</b-button>
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
        <b-modal hide-header-close no-close-on-backdrop @ok="handleConfirm" ref="confirm-modal" ok-title="Confirm" title="Please confirm the date and time:">
            <b-container class="text-center">
                <b-row>
                    <b-col>The message will be sent at</b-col>
                </b-row>
                <b-row>
                <b-col class="m-4"><b>{{this.time}}@{{this.date}}</b></b-col>
                </b-row>
                <b-row>
                    <b-col>Is this correct?</b-col>
                </b-row>
            </b-container>
        </b-modal>
    </b-container>
</div>
</template>

<script>
export default {
    name: "SendMessage",
    data() {
        return {
            showSchedule: false,
            date: '',
            time: '',
            dateContext: null,
            timeContext: null
        }
    },
    methods: {
        handleSchedule() {
            if (this.showSchedule) {
                this.showSchedule = false
            } else {
                this.showSchedule = true
            }
        },

        handleReset() {
            this.dateContext = null
            this.timeContext = null
            this.date = ""
            this.time = ""
        },

        handleSave() {
            if(this.date != "" && this.time != "") {
                this.$refs['confirm-modal'].show()
            }
        }, 

        handleConfirm() {

        },

        onDateContext(ctx) {
            this.dateContext = ctx
        },

        onTimeContext(ctx) {
            this.timeContext = ctx
        }
    }

}
</script>

<style>

#or {
    font-family: Geraldine;
    font-size: 50px;
}

#schedule {
    margin-left: 7%;
}

#left-button {
    margin-right: 7%;
}

</style>