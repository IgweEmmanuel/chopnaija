// src/store/material.js
import { create } from 'zustand'

const useMaterialStore = create((set) => ({
  materials: [],
  setMaterials: (materials) => set({ materials }),
  addMaterial: (material) =>
    set((state) => ({ materials: [...state.materials, material] })),
}))

export default useMaterialStore
