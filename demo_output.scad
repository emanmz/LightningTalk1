union(){
    translate(v=[10, 0, 0]){
        union(){
            sphere(r=10, $fn=100);
            rotate(a=[0, 0, 45]){
                cube(size=[20, 10, 10]);
            };
        };
    };
    union(){
        cube(size=[10, 20, 10]);
        cube(size=[20, 10, 10]);
    };
    translate(v=[10, 10, 10]){
        cube(size=[10, 20, 10]);
    };
    color("#CC5500"){
        cube(size=[10, 20, 10]);
    };
};
