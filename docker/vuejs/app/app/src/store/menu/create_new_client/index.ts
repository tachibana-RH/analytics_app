import { Module } from 'vuex';
import { RootState } from '@/store/types';
import { ChildClientState } from './types'
import getters from './getters';
import actions from './actions';
import mutations from './mutations';

const state: ChildClientState = {
  f_client_name: "",
  f_category: "",
  f_client_origin: "",
  childclients: []
};

export const ChildClientModule: Module<ChildClientState, RootState> = {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};