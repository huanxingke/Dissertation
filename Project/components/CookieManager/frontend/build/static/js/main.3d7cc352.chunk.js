(this.webpackJsonpcookie_manager=this.webpackJsonpcookie_manager||[]).push([[0],{15:function(e,t,n){"use strict";n.r(t);var s=n(0),o=n.n(s),c=n(5),r=n.n(c),a=n(3),i=n(7),u=n(2),l=null,m=new i.a,d=Object(a.b)((function(e){var t=e.args,n=t.method,s=t.param,o=t.value,c=t.expires_at,r=null;return r="set"==n?function(e,t,n){return m.set(e,t,{path:"/",samesite:"strict",expires:new Date(n)}),{code:200,msg:"Set cookie "+e+"="+t+"."}}(s,o,c):"get"==n?function(e){var t=m.get(e)||null;return null==t?{code:404,msg:"Key Not Exist!"}:{code:200,msg:"Success.",value:t}}(s):"del"==n?function(e){return m.remove(e,{path:"/",samesite:"strict"}),{code:200,msg:"Delete cookie where param="+e+"."}}(s):{code:200,msg:"Success.",cookies:m.getAll()},r&&JSON.stringify(l)!=JSON.stringify(r)&&(l=r,a.a.setComponentValue(r),a.a.setComponentReady()),Object(u.jsx)("div",{})}));r.a.render(Object(u.jsx)(o.a.StrictMode,{children:Object(u.jsx)(d,{})}),document.getElementById("root"))}},[[15,1,2]]]);
//# sourceMappingURL=main.3d7cc352.chunk.js.map