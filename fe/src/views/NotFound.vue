<template>
<div>
    <b-container>
        <b-row>
            <b-col>
                <img id="cat" src="../assets/img/404cat.jpg" />
            </b-col>
            <b-col>
                <b-row id="rest">
                    <b-col id="oops" class="text-center">
                        Oops...
                    </b-col>
                </b-row>
                <b-row>
                    <b-col class="text-center">
                        That was awkward.
                    </b-col>
                </b-row>
                <b-row>
                    <b-col id="notfound" class="text-center">
                        Sorry, but your page wasn't found.
                    </b-col>
                </b-row>
            </b-col>
        </b-row>
    </b-container>
</div>
</template>

<script>
export default {
    name: "NotFound"

}
</script>

<style>

#cat {
    width: 80%;
    margin-top: 20%
}

#rest {
    margin-top: 55%;
}

#oops {
    font-size: 80px;
}

#notfound {
    font-size: 40px;
}

</style>