<template>
  <v-footer
    absolute
    class="font-weight-medium"
  >
    <v-col class="blog-footer">
      <small>&copy; とまとエンジニア日記 {{ new Date().getFullYear() }}</small>
    </v-col>
  </v-footer>
</template>

<script>
  export default {
    data () {
      return {}
    }
  }
</script>

<style scoped>
  .blog-footer{
    text-align: center;
  }
</style>
