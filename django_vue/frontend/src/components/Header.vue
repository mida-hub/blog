<template>
  <v-container fluid>
    <v-row style="height: 30px;" dense>
      <v-col dense>
        <div class="blog-wapper">
          <h1 class="blog-title">
            とまとエンジニア日記
            <v-img
              width="35"
              style="float:left;"
              v-bind:src="require('@/assets/tomato.jpg')"
            ></v-img>
          </h1>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {}
    }
  }
</script>

<style scoped>
  .blog-title{
    text-align: center;
    margin: 10px;
  }

  .blog-wapper{
    display: flex;
    justify-content: center; 
  }

</style>
