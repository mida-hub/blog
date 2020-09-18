<template>
  <v-container fluid grid-list-md>
    <v-row
      justify="center"
      align-content="center"
      style="height: 50px;"
    >
      <v-col>
      </v-col>
      <v-col cols="8">
        <Tag></Tag>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
    <v-row
      justify="center"
      align-content="center"
    >
      <v-col>
      </v-col>
      <v-col cols="8">
        <Post></Post>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import Tag from '@/components/Tag'
  import Post from '@/components/Post'

  export default {
    components: {
      Tag,
      Post
    }
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
