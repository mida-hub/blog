<template>
  <v-container fluid grid-list-md>
    <v-row>
      <v-col>
      </v-col>
      <v-col>
        <Article></Article>
      </v-col>
      <v-col>
        <Category></Category>
        <Tag></Tag>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import Category from '@/components/Category'
  import Tag from '@/components/Tag'
  import Article from '@/components/Article'

  export default {
    components: {
      Category,
      Tag,
      Article
    }
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
  @import '../statics/style.css';
</style>
