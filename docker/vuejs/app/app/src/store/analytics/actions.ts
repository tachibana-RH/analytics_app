import { ActionTree } from 'vuex';
import { AnalyState, RootState, Analy } from '@/store/types';
import { ApiRqsV1 } from '../../methods/ApiRequestV1'

const actions: ActionTree<AnalyState, RootState> = {
  set: ({ commit }, data: Analy[]) => {
    commit('set', data);
    return true;
  },

  add: async ({ commit }, analy: Analy) => {
    await ApiRqsV1('POST', '/analytics/estimate', analy, false)
    .catch(err => {
      // 失敗
      console.error(err);
      return false;
    });
    // 成功
    commit('add', analy);
    return true;
  },

  remove: async ({ commit }, id: string) => {
    await ApiRqsV1('DELETE', '/analytics/estimate', {id: id}, false)
    .catch(err => {
      console.error(err);
      return false;
    });
    commit('remove', id);
    return true;
  },

};

export default actions;