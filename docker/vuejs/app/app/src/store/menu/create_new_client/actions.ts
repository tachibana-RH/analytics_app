import { ActionTree } from 'vuex';
import { RootState } from '@/store/types';
import { ChildClient, ChildClientState } from './types'
import { ApiRqsV1 } from '../../../methods/ApiRequestV1'

const actions: ActionTree<ChildClientState, RootState> = {
  set: ({ commit }, data: ChildClient[]) => {
    commit('set', data);
    return true;
  },

  add: async ({ commit }, data: ChildClient) => {
    commit('add', data);
    return true;
  },

  remove: async ({ commit }, index: number) => {
    commit('remove', index);
    return true;
  },

  regist: async ({ commit }, data: ChildClient[]) => {
    await ApiRqsV1('POST', '/menus/create/regist', data, false)
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