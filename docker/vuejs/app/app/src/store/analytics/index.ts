import { Module } from 'vuex';
import { AnalyState, RootState } from '@/store/types';
import getters from './getters';
import actions from './actions';
import mutations from './mutations';

const state: AnalyState = {
  analy: []
};

export const analys: Module<AnalyState, RootState> = {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};