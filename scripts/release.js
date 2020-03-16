const execa = require('execa')
const fs = require('fs')
const inquirer = require('inquirer')
const semver = require('semver')

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

const release = async() => {
  const curVersion = JSON
    .parse(fs.readFileSync('./package.json', 'utf8'))
    .version

  console.log(`[./scripts/release.js] Current version: st3-${curVersion}`)

  const bumps = ['major', 'minor', 'patch', 'prerelease']
  const versions = {}
  bumps.forEach(b => {
    versions[b] = semver.inc(curVersion, b)
  })
  const bumpChoices = bumps.map(b => ({ name: `${b} (${versions[b]})`, value: b }))

  const { bump } = await inquirer.prompt([
    {
      name: 'bump',
      message: 'Select release type:',
      type: 'list',
      choices: [
        ...bumpChoices
      ]
    }
  ])

  const version = versions[bump]

  const { yes } = await inquirer.prompt([
    {
      name: 'yes',
      message: `Confirm releasing st3-${version}?`,
      type: 'list',
      choices: ['Cancel', 'Ok']
    }
  ])

  if (yes === 'Cancel') {
    console.log('[./scripts/release.js] cancelled.')
    return
  }

  await execa('npm', ['--no-git-tag-version', 'version', version], { stdio: 'inherit' })
  await execa('git', ['add', '-A'], { stdio: 'inherit' })
  await execa('git', ['commit', '-m', `bump: Bump package from st3-${curVersion} to st3-${version}`], { stdio: 'inherit' })

//  Documentation and Changelog on master branch for ST4

  await execa('git', ['commit', '--allow-empty', '-S', '-m', `release: st3-${version}`], { stdio: 'inherit' })
  await execa('git', ['tag', '-s', `st3-${version}`, '-m', `st3-${version}`], { stdio: 'inherit' })
  await execa('git', ['push', 'origin', 'st3', '--tags'], { stdio: 'inherit' })

  console.log(`[./scripts/release.js] Done releasing version: st3-${version}`)
}

release().catch(err => {
  console.error(err)
  process.exit(1)
})
