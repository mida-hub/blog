<template>
  <v-container fluid>
    <v-row>
      <v-card-text>
        <div v-if="loading" class="text-center">
          <v-progress-circular
            :size="50"
            color="primary"
            indeterminate
            />
        </div>
        <div v-else-if="token">
          <div class="text-center">
            <v-btn 
              depressed
              class="pink white--text"
              @click="logout">
              Logout
            </v-btn>
          </div>
        </div>
        <div v-else>
          {{ token }}
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="credentials.username"
              :rules="rules.username"
              placeholder="example@domain.com"
              outlined
              label="email"
              maxlength="30"
              required
            />
            <v-text-field
              type="password"
              v-model="credentials.password"
              :rules="rules.password"
              placeholder="password"
              outlined
              label="password"
              maxlength="30"
              required
            />
            <div class="text-center">
              <v-btn 
                depressed
                class="pink white--text"
                :disabled="!valid"
                @click="login">
                Login
              </v-btn>
            </div>
          </v-form>
        </div>
      </v-card-text>
    </v-row>
  </v-container>
</template>

<script>
  import Swal from 'sweetalert2';

  export default {
    name: 'Auth',
    data: () => ({
      credentials: {},
      valid: true,
      loading: false,
      token: null,
      rules: {
        username: [
          v => !!v || "ユーザー名は必須です"
        ],
        password: [
          v => !!v || "パスワードは必須です"
        ]
      }
    }),
    methods: {
      login() {
        if (this.$refs.form.validate()) {
          this.loading = true
          this.$store.dispatch('login', this.credentials)
          .then(() => {
            this.token = this.$store.getters.getAuthToken
          })
          .catch((error) => {
            console.log(error)
            Swal.fire({
              icon: 'error',
              title: 'Login Error',
              text: 'email もしくは password が間違っています',
              showConfirmButton: false,
              showCloseButton: false,
              timer: 3000
            })
          })
          .finally(() => {
            this.loading = false;
          })
        }
      },
      logout() {
        this.$store.dispatch('logout')
        this.token = this.$store.getters.getAuthToken
      }
    },
    created: function () {
      this.token = this.$store.getters.getAuthToken
    }
}
</script>
<style scoped>
  .text-center{
    text-align: center; 
  }
</style>
