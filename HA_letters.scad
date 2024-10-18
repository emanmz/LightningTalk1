union(){
    translate(v=[0, 0, 0]){
        color("pink"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[20, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
                translate(v=[10, 25, 0]){
                    cube(size=[10, 10, 10]);
                };
            };
        };
    };
    translate(v=[50, 0, 0]){
        color("green"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[0, 40, 0]){
                    cube(size=[30, 10, 10]);
                };
                translate(v=[0, 25, 0]){
                    cube(size=[30, 10, 10]);
                };
                translate(v=[20, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
            };
        };
    };
};
