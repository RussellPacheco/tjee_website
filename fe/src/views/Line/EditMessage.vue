<template>
<div>
<b-container class="mt-5">
    <b-row>
        <b-col></b-col>
        <b-col class="title text-center">
            Edit Message
        </b-col>
        <b-col></b-col>
    </b-row>
</b-container>
<div class="newmessage-container">
    <b-container class="mt-5">
        <b-row>
            <b-col id="edit-message-details">
                <b-row >
                    <b-col>
                        <b-table striped :items="[this.$store.state.editMessage]" :fields="modalFields"></b-table>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="text-center">
                        <b class="message-title">Title</b>
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="text-center mt-3">
                        {{this.$store.state.editMessage.title}}
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="text-center mt-4">
                        <b class="message-title">Message</b>
                    </b-col>
                </b-row>
                <b-row class="text-center mt-3">
                    <b-col>{{this.$store.state.editMessage.message}}</b-col>
                </b-row>
            </b-col>
            <b-col>
                <b-form-textarea
                id="textarea"
                v-model="text"
                placeholder="Enter something..."
                rows="20"
                max-rows="20"
                ></b-form-textarea>
                <b-row class="mt-1">
                    <b-col><b-button variant="danger" @click="clearMessage">Clear</b-button></b-col>
                    <b-col></b-col>
                    <b-col class="d-flex mt-2 flex-row-reverse">
                        <b-button v-b-modal.confirm-modal>Save Message</b-button>
                        <b-modal hide-header-close no-close-on-backdrop @ok="handleOk" ok-title="Save" id="confirm-modal" title="Are you sure you want to save this?">
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
        </b-row>
    </b-container>
</div>
</div>
</template>

<script>
export default {
    name: "EditMessage",
    data() {
        return {
            editingMessage: this.$store.state.editMessage,
            text: this.$store.state.editMessage.message,
            modalFields: [
                {key:"num_id", label:"ID"}, 
                {key: "created_by_name", label: "Creator"}, 
                {key: "created_at"}, 
                {key: "last_sent"}
            ],
        }
    },

    methods: {
        handleOk() {
            this.editingMessage.message = this.text
            this.$store.dispatch("saveEditedMessage", this.editingMessage)


        },

        clearMessage() {
            this.text = ""
        }
    }

}
</script>

<style>

#edit-message-details {
    border: 1px solid;
    border-color: lightgray;
    border-radius: 3px;
}

.message-title {
    text-decoration: underline;
}


</style>