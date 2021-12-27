<template>
<div>
  <Header />
  <b-container fluid>
    <b-row class="justify-content-center">
      <b-col v-if="adminLogin">
      </b-col>
      <b-col cols="8">
        <router-view></router-view>
      </b-col>
    </b-row>
  </b-container>
</div>
</template>

<script>
import Header from "./components/Header.vue"

export default {
  name: "App",
  components: {
    Header
  }
  
}
</script>


<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.main {
  display: flex;
  justify-content: center;
}


</style>
