import { ActionTree } from 'vuex';
import { RootState } from '@/store/types'
import { ClientState, Client } from './types';
import { ApiRqsV1 } from '../../../methods/ApiRequestV1'

const actions: ActionTree<ClientState, RootState> = {
  set: ({ commit }) => {
    ApiRqsV1('GET', '/menu/top', undefined, false)
    .then(res => {
      // 成功
      commit('set', res['data']);
      return true;
    })
    .catch(err => {
      // 失敗
      console.error(err);
      return false;
    });
  },

  add: async ({ commit }, data: Client) => {
    await ApiRqsV1('POST', '/menu/new', data, false)
    .catch(err => {
      // 失敗
      console.error(err);
      return false;
    });
    // 成功
    commit('add', data);
    return true;
  },

  remove: async ({ commit }, id: string) => {
    await ApiRqsV1('DELETE', '/menu/delete', {f_client_id: id}, false)
    .catch(err => {
      // 失敗
      console.error(err);
      return false;
    });
    // 成功
    commit('remove', id);
    return true;
  },

};

export default actions;