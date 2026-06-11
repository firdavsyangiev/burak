import mongoose, { Schema } from "mongoose";
import {
  ProductCollection,
  ProductStatus,
  ProductSize,
  ProductVolume,
} from "../libs/enums/product.enum";

const productSchema = new Schema(
  {
    ProductStatus: {
      type: String,
      enum: ProductStatus,
      default: ProductStatus.PAUSE,
    },

    ProductCollection: {
      type: String,
      enum: ProductCollection,
      reuired: true,
    },

    productName: {
      type: String,
      required: true,
    },

    productPrice: {
      type: Number,
      required: true,
    },

    productLeftCount: {
      type: Number,
      required: true,
    },

    productSize: {
      type: String,
      enum: ProductSize,
      default: ProductSize.NORMAL,
    },

    productVolume: {
      type: String,
      enum: ProductVolume,
      default: ProductVolume.ONE,
    },

    productDesc: {
      type: String,
      required: true,
    },

    productImage: {
      type: [String],
      default: [],
    },

    productView: {
      type: Number,
      default: 0,
    },
  },
  { timestamps: true }, // createdAt, updatedAt
);

productSchema.index(
  { productName: 1, productSize: 1, productVolume: 1 },
  { unique: true },
);
export default mongoose.model("Product", productSchema);
