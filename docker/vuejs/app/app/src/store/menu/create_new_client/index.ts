import { Module } from 'vuex';
import { RootState } from '@/store/types';
import { ClientChildState } from './types'
import getters from './getters';
import actions from './actions';
import mutations from './mutations';

const state: ClientChildState = {
  f_client_name: "",
  f_category: "",
  f_client_origin: "",
  clientchilds: []
};

export const ClientChildModule: Module<ClientChildState, RootState> = {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};