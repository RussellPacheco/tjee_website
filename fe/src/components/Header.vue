<template>
<div>
    <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
            <b-nav-item :to="{name: 'Home'}">Home</b-nav-item>

            <!-- Navbar dropdowns -->
            <b-nav-item-dropdown text="Menu" right>
            <b-dropdown-item href="#">Open</b-dropdown-item>
            <b-dropdown-item href="#">Edit</b-dropdown-item>
            <b-dropdown-item href="#">Options</b-dropdown-item>
            <b-dropdown-item href="#">Exit</b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown text="User" right>
            <b-dropdown-item :to="{name: 'Login'}">Login</b-dropdown-item>
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