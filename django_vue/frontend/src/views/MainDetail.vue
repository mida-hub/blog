<template>
  <v-container fluid>
    <v-row>
      <v-col>
      </v-col>
      <v-col cols="8">
        <PostDetail></PostDetail>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import PostDetail from '@/components/PostDetail'

  export default {
    components: {
      PostDetail
    }
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
</style>
