<template>
<div>
    <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
            <b-nav-item v-if="!isAuthenticated" :to="{name: 'Home'}">Home</b-nav-item>
            <b-nav-item-dropdown v-if="isAuthenticated" text="Home" left>
                <b-dropdown-item :to="{name: 'Home'}">Home</b-dropdown-item>
                <b-dropdown-item :to="{name: 'Admin'}">Admin</b-dropdown-item>
            </b-nav-item-dropdown>
            <!-- Navbar dropdowns -->
            <b-nav-item-dropdown v-if="isAuthenticated" text="Members" left>
                <b-dropdown-item :to="{name: 'NewMember'}">Add New Member</b-dropdown-item>
                <b-dropdown-item :to="{name: 'ViewMembers'}">View/Edit Members</b-dropdown-item>
                <b-dropdown-item href="#">View Pending Applications</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown v-if="isAuthenticated" text="Line" left>
            <b-dropdown-item :to="{name: 'NewMessage'}">New Message</b-dropdown-item>
            <b-dropdown-item :to="{name: 'ViewMessages'}">View/Edit Messages</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown v-if="isAuthenticated" text="Bot" left>
            <b-dropdown-item :to="{name: 'Permissions'}">Permissions</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown text="User" left>
            <b-dropdown-item v-if="!isAuthenticated" :to="{name: 'Login'}">Login</b-dropdown-item>
            <b-dropdown-item v-if="isAuthenticated" :to="{name: 'Settings'}">Settings</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar-nav>
    </b-navbar>
</div>
</template>

<script>
export default {
    name: "Header",
    computed: {
        isAuthenticated () {
            return this.$store.getters.isAuthenticated
    }
  }


}
</script>

<style>

</style>