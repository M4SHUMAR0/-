window.onload=function(){
    console.log("読み込み完了")
    let q1,q2,q3;

    q1=document.getElementById("q1");

    let price,personality,pace,member;
    price=document.getElementById("price");
    personality=document.getElementById("personality");
    pace=document.getElementById("pace");
    member=document.getElementById("member");
    
    personality.classList.add("blind");
    pace.classList.add("blind");
    member.classList.add("blind");

    console.log(q2,q3,price,personality,pace,member);

    q1.onclick=function(){
        price.classList.add("blind");
        personality.classList.remove("blind");
        q2=document.getElementById("q2");
        
        q2.onclick=function(){
            personality.classList.add("blind");
            pace.classList.remove("blind");
            q3=document.getElementById("q3");

            q3.onclick=function(){
                pace.classList.add("blind");
                member.classList.remove("blind");
            };
        };
    };

};