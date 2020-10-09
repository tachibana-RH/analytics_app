import { MutationTree } from 'vuex';
import { AnalyState, Analy } from '@/store/types';

const mutations: MutationTree<AnalyState> = {
  set: (state, data: Analy[]) => {
    state.analy = data;
  },
  add: (state, data: Analy) => {
    state.analy.push(data);
  },
  remove: (state, id: string) => {
    state.analy = state.analy.filter((e: Analy) => e.id !== id);
  },
};

export default mutations;