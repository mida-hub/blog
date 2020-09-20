<template>
  <v-container fluid>
    <v-row class="blog-title-row">
      <v-col>
        <div class="blog-title-wapper">
          <h1 class="blog-title-name">
            とまとエンジニア日記
            <v-img class="blog-title-img"
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
  .blog-title-row{
    height: 30px;
  }

  .blog-title-wapper{
    display: flex;
    justify-content: center; 
  }

  .blog-title-name{
    text-align: center;
    margin: 10px;
  }

  .blog-title-img{
    float: left;
    width: 35px;
  }
</style>
