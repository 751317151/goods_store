/*
 * @Author: 华豪
 * @Date: 2019-09-25 19:23:26
 * @E-Mail: hh@huahaohh.cn
 * @LastEditors: 华豪
 * @LastEditTime: 2019-09-25 19:23:26
 */
function getvalue1(simple){  
    if (simple === 'sno'){   
        $('.inp').attr('placeholder',"请输入编号");
        $("#update_action").attr('action','update');
        $(".inp").attr('name','upd_sno');
    }
    else if (simple === 'name'){   
        $('.inp').attr('placeholder',"请输入名称");
        $("#update_action").attr('action','update2');
        $(".inp").attr('name','upd_name');
    }
}

function getvalue2(simple){  
    if (simple === 'sno'){   
        $('.inp').attr('placeholder',"请输入编号");
        $("#find_action").attr('action','find');
        $(".inp").attr('name','find_sno');
    }
    else if (simple === 'name'){   
        $('.inp').attr('placeholder',"请输入名称");
        $("#find_action").attr('action','find2');
        $(".inp").attr('name','find_name');
    }
    else if (simple === 'all'){   
        $('.inp').attr('placeholder',"查询所有");
        $("#find_action").attr('action','find3');
    }
}

function getvalue3(simple){  
    if (simple === 'sno'){   
        $('.inp').attr('placeholder',"请输入编号");
        $("#del_action").attr('action','del1');
        $(".inp").attr('name','del_sno');
    }
    else if (simple === 'name'){   
        $('.inp').attr('placeholder',"请输入名称");
        $("#del_action").attr('action','del2');
        $(".inp").attr('name','del_name');
    }
}