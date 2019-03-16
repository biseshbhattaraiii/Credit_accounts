import Vue from 'vue'
import Router from 'vue-router'
import CreditMain from '@/components/CreditMain'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'CreditMain',
      component: CreditMain
    }
  ]
})
