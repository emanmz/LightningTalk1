union(){
    translate(v=[0, 0, 0]){
        color("red"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[0, 40, 0]){
                    cube(size=[30, 10, 10]);
                };
                translate(v=[0, 20, 0]){
                    cube(size=[20, 10, 10]);
                };
                translate(v=[0, 0, 0]){
                    cube(size=[30, 10, 10]);
                };
            };
        };
    };
    translate(v=[50, 0, 0]){
        color("blue"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[20, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
                translate(v=[10, 25, 0]){
                    cube(size=[10, 15.0, 10]);
                };
            };
        };
    };
    translate(v=[100, 0, 0]){
        color("red"){
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
    translate(v=[150, 0, 0]){
        color("blue"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[20, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
                translate(v=[21, 0, 0]){
                    rotate(a=[0, 0, 25]){
                        cube(size=[10, 50, 10]);
                    };
                };
            };
        };
    };
};
