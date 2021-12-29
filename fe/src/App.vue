<template>
<div>
  <Header />
  <b-container fluid>
    <b-row class="router justify-content-center">
      <b-col>
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
    Header,
  }
  
}
</script>


<style>
@font-face {
  font-family: Geraldine;
  src: url("./assets/font/GeraldinePersonalUseItalic-PK12m.ttf");
}

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
