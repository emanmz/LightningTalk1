union(){
    translate(v=[0, 0, 0]){
        color("red"){
            union(){
                translate(v=[10, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
                translate(v=[0, 40, 0]){
                    cube(size=[30, 10, 10]);
                };
                translate(v=[0, 0, 0]){
                    cube(size=[30, 10, 10]);
                };
            };
        };
    };
    translate(v=[100, 0, 0]){
        color("orange"){
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
        color("yellow"){
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
    translate(v=[250, 0, 0]){
        color("green"){
            union(){
                cube(size=[30, 10, 10]);
                translate(v=[0, 10, 0]){
                    cube(size=[10, 30, 10]);
                };
                translate(v=[0, 40, 0]){
                    cube(size=[30, 10, 10]);
                };
                translate(v=[30, 0, 0]){
                    cube(size=[10, 20, 10]);
                };
            };
        };
    };
    translate(v=[300, 0, 0]){
        color("blue"){
            union(){
                cube(size=[10, 50, 10]);
                translate(v=[10, 30, 0]){
                    cube(size=[20, 20, 10]);
                };
                translate(v=[10, 33.333333333333336, 0]){
                    rotate(a=[0, 0, -150]){
                        cube(size=[10, 33.333333333333336, 10]);
                    };
                };
            };
        };
    };
    translate(v=[350, 0, 0]){
        color("purple"){
            translate(v=[10, 20.0, 0]){
                difference(){
                    cylinder(h=10, r=20);
                    translate(v=[0, 0, -0.5]){
                        cylinder(h=11, r=10);
                    };
                };
            };
        };
    };
    translate(v=[400, 0, 0]){
        color("red"){
            translate(v=[10, 20.0, 0]){
                difference(){
                    cylinder(h=10, r=20);
                    translate(v=[0, 0, -0.5]){
                        cylinder(h=11, r=10);
                    };
                };
            };
        };
    };
    translate(v=[450, 0, 0]){
        color("orange"){
            union(){
                translate(v=[10, 0, 0]){
                    cube(size=[10, 50, 10]);
                };
                translate(v=[0, 40, 0]){
                    cube(size=[30, 10, 10]);
                };
            };
        };
    };
    translate(v=[500, 0, 0]){
        color("yellow"){
            translate(v=[0, 20, 0]){
                union(){
                    cube(size=[10, 50, 10]);
                    translate(v=[0, -20, 0]){
                        cube(size=[10, 10, 10]);
                    };
                };
            };
        };
    };
};
