import { GetterTree } from 'vuex';
import { AnalyState, RootState } from '@/store/types';

const getters: GetterTree<AnalyState, RootState> = {
  size: (state: AnalyState) => {
    return state.analy.length;
  },
  data: (state: AnalyState) => {
    return state.analy
  }
};

export default getters;