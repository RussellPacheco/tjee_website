<template>
  <div class="home-container">
    <b-container>
      <b-row>
        <b-col></b-col>
        <b-col class="text-center mt-5" id="logo">Welcome to TJEE!</b-col>
        <b-col></b-col>       
      </b-row>
      <b-row>
        <b-col></b-col>
        <b-col class="d-flex justify-content-center"><img src="../assets/img/construction.jpg" id="construction"/></b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  }
}
</script>

<style>

#logo {
  font-size: 50px;
}

#construction {
  height: 20%;
}

</style>
