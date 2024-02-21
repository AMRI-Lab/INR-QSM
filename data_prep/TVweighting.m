function WG=TVweighting(phase,Mask,spatial_resolution,TV_range)
    x0=phase;
    Mask4D=repmat(Mask,[1 1 1 3]);
    GRAD(:,:,:,1) = x0([2:end,end],:,:) - x0;
    GRAD(:,:,:,2) = x0(:,[2:end,end],:) - x0;
    GRAD(:,:,:,3) = x0(:,:,[2:end,end]) - x0;
    GRAD=abs(GRAD);
    GRAD_Sort=sort(GRAD(Mask4D==1));
    PhiGDPhigh=GRAD_Sort(round(length(GRAD_Sort)*TV_range(2)));
    PhiGDPlow=GRAD_Sort(round(length(GRAD_Sort)*TV_range(1)));
    WG1=(PhiGDPhigh-GRAD)/(PhiGDPhigh-PhiGDPlow);
    WG1(WG1>1)=1;
    WG1(WG1<0)=0;
    WG=WG1.*Mask4D;

end