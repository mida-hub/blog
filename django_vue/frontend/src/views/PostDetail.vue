<template>
  <v-container fluid>
    <v-row>
      <v-col>
      </v-col>
      <v-col cols="8">
        <Category></Category>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import Category from '@/components/Category'

  export default {
    components: {
      Category
    }
  }
</script>

<style scoped>
  @import '../statics/normalize.css';
</style>
