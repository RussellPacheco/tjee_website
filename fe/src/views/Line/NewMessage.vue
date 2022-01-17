<template>
<div>
<b-container class="mt-5">
    <b-row>
        <b-col></b-col>
        <b-col class="title text-center">
            New Message
        </b-col>
        <b-col></b-col>
    </b-row>
</b-container>
<div class="newmessage-container">
    <b-container class="mt-5">
        <b-row>
            <b-col></b-col>
            <b-col cols="6">
                <b-input placeholder="Write a title..." v-model="title"></b-input>
                <b-form-textarea
                id="textarea"
                v-model="text"
                placeholder="Enter something..."
                rows="8"
                max-rows="20"
                ></b-form-textarea>
                <b-row class="mt-1">
                    <b-col><b-button variant="danger" @click="clearMessage">Clear</b-button></b-col>
                    <b-col></b-col>
                    <b-col class="d-flex mt-2 flex-row-reverse">
                        <b-button v-b-modal.confirm-modal>Save Message</b-button>
                        <b-modal ref="confirmModal" size="lg" hide-header-close no-close-on-backdrop @ok="handleOk" id="confirm-modal" title="Confirm Your Message">
                            <b-container>
                                <b-row>
                                    <b-col></b-col>
                                    <b-col class="text-center" cols="8">
                                        {{text}}
                                    </b-col>
                                    <b-col></b-col>
                                </b-row>
                            </b-container>
                        </b-modal>
                    </b-col>
                </b-row>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>
</div>
</div>
</template>

<script>
export default {
    name: "NewMessage",
    data() {
        return {
            text: "",
            title: ""
        }
    },

    methods: {
        handleOk() {
            const payload = {
                created_by: this.$store.state.currentAdmin.member_id,
                message: {title: this.title, body: this.text}
            }
            this.$store.dispatch("saveLineMessage", payload)
            this.$refs['confirmModal'].hide('confirm-modal')
        },

        clearMessage() {
            this.text = ""
        }
    }

}
</script>

<style>

.title {
    font-size: 50px;
    border-bottom: 1px solid;
}

</style>