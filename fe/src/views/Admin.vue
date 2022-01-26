<template>
<div>
<b-container class="mt-5 mb-5">
        <b-row>
            <b-col></b-col>
            <b-col class="title text-center">
                Administration
            </b-col>
            <b-col></b-col>
        </b-row>
        <b-row>
            <b-col class="text-center">Welcome <b>{{this.$store.state.currentAdmin.username}}</b>! Click on the selection to view more details</b-col>
        </b-row>
</b-container>
<b-container>
    <b-row>
        <b-col></b-col>
        <b-col cols="8">
            <div class="accordion" role="tablist">
                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button class="admin-button" block v-b-toggle.adminAccordion-members variant="light">Members</b-button>
                    </b-card-header>
                    <b-collapse id="adminAccordion-members" accordion="admin-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group flush>
                                <b-list-group-item :to="{name: 'NewMember'}">
                                    <b>Add New Member</b> - Add a new member to the TJEE family! 
                                </b-list-group-item>
                                <b-list-group-item :to="{name: 'ViewMembers'}">
                                    <b>Edit/View Member</b> - View all members and edit a specific member's details.
                                </b-list-group-item>
                                <b-list-group-item :to="{name: 'ViewPendingMembers'}">
                                    <b>View Pending Applications</b> - View all pending applications from Meetup. 
                                </b-list-group-item>                      
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button class="admin-button" block v-b-toggle.adminAccordion-line variant="light">Line</b-button>
                    </b-card-header>
                    <b-collapse id="adminAccordion-line" accordion="admin-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group flush>
                                <b-list-group-item :to="{name: 'NewMessage'}">
                                    <b>Add New Message</b> - Create and save a new Line Group message. 
                                </b-list-group-item>
                                <b-list-group-item :to="{name: 'ViewMessages'}">
                                    <b>Edit/View Messages</b> - View all Line Messages and edit a specific message.
                                </b-list-group-item>                
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button class="admin-button" block v-b-toggle.adminAccordion-bot variant="light">Bot</b-button>
                    </b-card-header>
                    <b-collapse id="adminAccordion-bot" accordion="admin-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group flush>
                                <b-list-group-item :to="{name: 'Permissions'}">
                                    <b>Modify Bot Permissions</b> - Turn on or off bot permissions for doing things like allowing a bot to join a new line group. 
                                </b-list-group-item>          
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
                <b-card no-body class="mb-1">
                    <b-card-header header-tag="header" class="p-1" role="tab">
                        <b-button class="admin-button" block v-b-toggle.adminAccordion-settings variant="light">User Settings</b-button>
                    </b-card-header>
                    <b-collapse id="adminAccordion-settings" accordion="admin-accordion" role="tabpanel">
                        <b-card-body>
                            <b-list-group flush>
                                <b-list-group-item :to="{name: 'Settings'}">
                                    <b>Settings</b> - Change your password or add a new admin. 
                                </b-list-group-item>          
                            </b-list-group>
                        </b-card-body>
                    </b-collapse>
                </b-card>
            </div>
        </b-col>
        <b-col></b-col>
    </b-row>
</b-container>
</div>  
</template>

<script>
export default {
    name: "Admin",
    methods: {
        handleRouter(route) {
            this.$router.push({name: route})
        }
    }

}
</script>

<style>

.admin-button {
    font-weight: bold;
}

.admin-border {
    border-bottom: 1px solid gray;
}

</style>