<template>
  <v-container>
    <v-parallax
      dark
      class="content-row"
      src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    >
      <v-row justify="center" align="center">
        <v-col cols="12" sm="8" md="6">
          <div class="text-center">
            <h1>Appear</h1>
            <p>Appear is a CLI toolkit to generate application code.</p>
          </div>
        </v-col>
      </v-row>
    </v-parallax>
    <v-row justify="space-around" class="content-row">
      <v-col>
        <v-card color="#385F73" dark>
          <v-card-title class="text-h5"> Reduce Project Cost </v-card-title>

          <v-card-subtitle
            >Swiftly write application code by leaving the repeatable tasks for
            a generator.</v-card-subtitle
          >

          <v-card-actions>
            <v-btn text> View the Schemas </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col>
        <v-card color="#385F73" dark>
          <v-card-title class="text-h5"> Longer Project Life </v-card-title>

          <v-card-subtitle
            >Improve maintainability by making the application files
            consistent.</v-card-subtitle
          >

          <v-card-actions>
            <v-btn text> Learn about Templates </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col>
        <v-card color="#385F73" dark>
          <v-card-title class="text-h5"> Frustration Be Gone </v-card-title>

          <v-card-subtitle
            >Reduce copy-paste errors or dangling unused code by
            design.</v-card-subtitle
          >

          <v-card-actions>
            <v-btn text> Learn More </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <p>
        For more information on Appear, check out the
        <a
          href="https://github.com/zacpez/appear"
          target="_blank"
          rel="noopener noreferrer"
        >
          documentation </a
        >.
      </p>
    </v-row>
    <v-row justify="center">
      <p>
        Find a bug? Report it on the github
        <a
          href="https://github.com/zacpez/appear/issues"
          target="_blank"
          rel="noopener noreferrer"
          title="contribute"
        >
          issue board </a
        >.
      </p>
    </v-row>
  </v-container>
</template>

<script>
export default {}
</script>
