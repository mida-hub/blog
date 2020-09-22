<template>
  <v-card height="56" outlined>
    <v-footer
      absolute
      class="grey lighten-2"
    >
      <v-col class="blog-footer">
        <small>&copy; とまとエンジニア日記 {{ new Date().getFullYear() }}</small>
      </v-col>
    </v-footer>
  </v-card>
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
