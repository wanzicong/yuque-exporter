





com.vip8.outway.api.service.kuaishou.KsRefundFacadeService

```plain

    /**
     * 售后信息列表
     * @param param
     * @return
     */
    ServiceResult<List<RefundDetailDTO>> getRefundDetailListByOid(RefundDetailParam param);
```





```plain

    @Override
    public ServiceResult<List<RefundDetailDTO>> getRefundDetailListByOid(RefundDetailParam param) {
        List<RefundDetailDTO> resultList = new ArrayList<>();
        AssertUtils.isNotNull(param.getSellerId(), "outway:参数sellerId不能为空");
        AssertUtils.isNotNull(param.getOid(), "outway:参数订单id不能为空");
        log.info("【获取售后详情列表】，param：{}", param);
        KuaishouAppInfoEntity appInfo = kuaishouAppInfoService.getBySellerId(param.getSellerId());
        if (appInfo != null) {
            try {
                OpenOrderDetailRequest orderDetailRequest = new OpenOrderDetailRequest();
                orderDetailRequest.setOid(param.getOid());
                OrderDetail orderDetail = kuaiShouClient.getorderDetailV2(appInfo, orderDetailRequest);
                if (orderDetail != null && orderDetail.getOrderRefundList() != null) {
                    for (OrderRefundInfo orderRefundInfo : orderDetail.getOrderRefundList()) {
                        Long refundId = orderRefundInfo.getRefundId();
                        OpenSellerOrderRefundDetailRequest refundDetailRequest = new OpenSellerOrderRefundDetailRequest();
                        refundDetailRequest.setRefundId(refundId);
                        MerchantRefundDetailDataView merchantRefundDetailDataView = kuaiShouClient.refundDetail(appInfo, refundDetailRequest);
                        if (merchantRefundDetailDataView != null) {
                            // 退款基本信息
                            KuaishouRefundOrderDetailEntity convert = KsRefundConvert.convert(merchantRefundDetailDataView);
                            resultList.add(OrikaMapperUtils.map(convert,RefundDetailDTO.class));
                        }
                    }
                }
            } catch (Exception e) {
                log.error("getRefundDetailList 异常 , param:{}", JSON.toJSONString(param),e);
            }
        }
        if (appInfo == null || resultList.size() == 0) {
            LambdaQueryWrapper<KuaishouRefundOrderDetailEntity> queryWrapper = new LambdaQueryWrapper<>();
            queryWrapper.eq(KuaishouRefundOrderDetailEntity::getOid,param.getOid());
            List<KuaishouRefundOrderDetailEntity> list = kuaishouRefundOrderDetailService.list(queryWrapper);
            for (KuaishouRefundOrderDetailEntity detailEntity : list) {
                resultList.add(OrikaMapperUtils.map(detailEntity,RefundDetailDTO.class));
            }
        }
        return new ServiceResult<>(resultList);
    }

```



```plain
package com.vip8.outway.api.result.kuaishou;

import lombok.Data;

@Data
public class RefundDetailDTO {
    private Long refundId;
    private Long oid;
    private Long skuId;
    private Long refundFee;
    private Integer status;
    private Long buyerId;
    private Long sellerId;
    private Integer handlingWay;
    private Integer refundType;
    private Integer refundReason;
    private String refundDesc;
    private Long logisticsId;
    private String pictures;
    private Long submitTime;
    private Long createTime;
    private Long updateTime;
    private Long relSkuId;
    private Long relItemId;
    private Integer sellerDisagreeReason;
    private String sellerDisagreeDesc;
    private String sellerDisagreeImages;
    private Integer negotiateStatus;
    private String negotiateReason;
    private Long negotiateUpdateTime;
    private Long timeLimitNegotiateChange;
    private Long validNegotiateBuyerModifyTimeStamp;
    private String expressNo;
    private Integer expressCode;
    private String logisticsCode;
    private Long expireTime;
    private Long endTime;
    private Long itemId;
    private Integer receiptStatus;
    private Long tradeOrderCreateTime;
    private String address;
    private String skuNick;
    private String refundReasonDesc;
    private String buyerOpenId;
}

```

