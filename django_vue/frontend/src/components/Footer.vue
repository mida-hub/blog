<template>
  <v-card height="50">
    <v-footer
      absolute
      class="font-weight-medium"
    >
      <v-col>
        <div class="blog-footer">
          <small>&copy; とまとエンジニア日記 {{ new Date().getFullYear() }}</small>
        </div>
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
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
