import { ActionTree } from 'vuex';
import { RootState } from '@/store/types';
import { ClientChild, ClientChildState } from './types'
import { ApiRqsV1 } from '../../../methods/ApiRequestV1'

const actions: ActionTree<ClientChildState, RootState> = {
  set: ({ commit }, data: ClientChild[]) => {
    commit('set', data);
    return true;
  },

  add: async ({ commit }, data: ClientChild) => {
    commit('add', data);
    return true;
  },

  remove: async ({ commit }, index: number) => {
    commit('remove', index);
    return true;
  },

  regist: async ({ commit }, data: ClientChild[]) => {
    await ApiRqsV1('POST', '/menu/create/regist', data, false)
    .catch(err => {
      // 失敗
      console.error(err);
      return false;
    });
    // 成功
    commit('regist');
    return true;
  },

};

export default actions;