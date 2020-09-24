<template>
  <v-container fluid>
    <v-row>
      <v-col>
      </v-col>
      <v-col cols="8">
        <Auth></Auth>
      </v-col>
      <v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import Auth from '@/components/Auth'

  export default {
    components: {
      Auth
    }
  }
</script>

<style scoped>
</style>
