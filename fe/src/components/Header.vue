<template>
<div>
    <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
            <b-nav-item :to="{name: 'Home'}">Home</b-nav-item>

            <!-- Navbar dropdowns -->
            <b-nav-item-dropdown v-if="this.$store.state.adminLogin" text="Members" left>
            <b-dropdown-item :to="{name: 'NewMember'}">Add</b-dropdown-item>
            <b-dropdown-item href="#">Edit</b-dropdown-item>
            <b-dropdown-item href="#">View</b-dropdown-item>
            <b-dropdown-item href="#">Pending</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown v-if="this.$store.state.adminLogin" text="Line" left>
            <b-dropdown-item :to="{name: 'NewMessage'}">New Message</b-dropdown-item>
            <b-dropdown-item :to="{name: 'ViewMessages'}">View/Edit Messages</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown v-if="this.$store.state.adminLogin" text="Bot" left>
            <b-dropdown-item :to="{name: 'Permissions'}">Permissions</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown text="User" left>
            <b-dropdown-item v-if="!this.$store.state.adminLogin" :to="{name: 'Login'}">Login</b-dropdown-item>
            <b-dropdown-item>Settings</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar-nav>
    </b-navbar>
</div>
</template>

<script>
export default {
    name: "Header",


}
</script>

<style>

</style>